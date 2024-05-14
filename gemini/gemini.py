import time
from functools import wraps

import google.generativeai as genai

from constants.ModelsConstants import gemini_constants_instance
from logs.log_config import configure_logger

logger = configure_logger(__name__)


gci = gemini_constants_instance


def retry(max_attempts=3, delay_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed. Retrying...")
                    time.sleep(delay_seconds)
            raise Exception(f"Failed after {max_attempts} attempts: {last_exception}")

        return wrapper

    return decorator


def get_gemini_prompt_example():
    file_name = gci.prompt_examples
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            file_content = ""
            while True:
                chunk = file.read(gci.chunk_size)
                if not chunk:
                    break
                file_content += chunk
            return file_content
    except IOError as e:
        logger.error(f"Error while trying to open the file {file_name}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


class Gemini:
    def __init__(self):
        genai.configure(api_key=gci.gemini_api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def describe_probabilities(self, predicted: dict, model_type: str):
        prompt = f"Doença: {predicted['class']} com probabilidade: {predicted['confidence']:.2f}%.\n"
        prompt += f"Model Type: {model_type}. Threshold: {gci.threshold}%.\n"
        examples = get_gemini_prompt_example()
        prompt += examples
        return prompt

    @retry(max_attempts=gci.max_attempts, delay_seconds=gci.delay_seconds)
    def generate_text(self, predicted: dict, model_type: str):
        prompt = self.describe_probabilities(predicted, model_type)
        response = self.model.generate_content(prompt)
        return response.text

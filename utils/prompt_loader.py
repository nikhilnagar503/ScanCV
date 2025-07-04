import json 
import os

class PromptLoader:
     """Class to load and format prompts from a JSON file."""
     def __init__(self, prompts_file, logger):
        self.prompts_file = prompts_file
        self.logger = logger
        self.logger.debug("Initializing PromptLoader with file: %s", self.prompts_file)
        self.prompts = self._load_prompts()



     def _load_prompts(self):
            """Load prompts from the JSON file."""
            try:
                self.logger.debug("Checking if prompts file exists: %s", self.prompts_file)
                if not os.path.exists(self.prompts_file):
                    self.logger.error("Prompts file not found: %s", self.prompts_file)
                    raise FileNotFoundError(f"Prompts file not found: {self.prompts_file}")

                with open(self.prompts_file, "r", encoding="utf-8") as f:
                    prompts = json.load(f)
                
                self.logger.debug("Prompts loaded successfully from %s", self.prompts_file)
                return prompts

            except Exception as e:
                self.logger.exception("Failed to load prompts from JSON.")
                raise Exception(f"Error loading prompts: {str(e)}")

            
            
            
     def get_prompt(self, prompt_key, **kwargs):
            if not hasattr(self, "prompts") or self.prompts is None:
                raise AttributeError("PromptLoader has no attribute 'prompts' because loading failed.")

            try:
                if prompt_key not in self.prompts:
                    self.logger.error("Prompt key not found: %s", prompt_key)
                    raise KeyError(f"Prompt key not found: {prompt_key}")
                template = self.prompts[prompt_key]["template"]
                return template.format(**kwargs)
            except Exception as e:
                self.logger.error("Error formatting prompt %s: %s", prompt_key, str(e))
                raise Exception(f"Error formatting prompt {prompt_key}: {str(e)}")

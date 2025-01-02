from transformers import pipeline

def load_ai_model():
    """
    Loads a pre-trained AI detection model from Hugging Face.
    This model will help in detecting AI-generated text.
    
    Returns:
        model (pipeline): The pre-trained model for AI text detection.
    """
    return pipeline('text-classification', model='bert-base-uncased')

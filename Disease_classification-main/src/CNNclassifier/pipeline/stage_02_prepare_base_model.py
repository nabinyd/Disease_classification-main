from CNNclassifier.congfig.configuration import ConfigurationManager
from CNNclassifier.components.prepare_base_model import PrepareBaseModel
from CNNclassifier import logger


STAGE_NAME="Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):           
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__== "__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>> Stage {STAGE_NAME} Started")
        obj=PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Finished")

    except Exception as e:
        logger.exception(e)
        raise e
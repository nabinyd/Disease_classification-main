from CNNclassifier import logger
from CNNclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNclassifier.pipeline.stage_03_training import ModelTrainingPipeline
from CNNclassifier.pipeline.stage_04_evaluation import EvaluationPipeline


STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=====x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Prepare Base Model"
try:
    logger.info(f"*************")
    logger.info(f">>>>> Stage {STAGE_NAME} Started")
    obj=PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Finished")

except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME= "Training"
if __name__== "__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>> Stage {STAGE_NAME} Started")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Finished")

    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Evaluaiton Stage"
if __name__== "__main__":
    try:
        logger.info(f"*************")
        logger.info(f">>>>> Stage {STAGE_NAME} Started")
        obj=EvaluationPipeline()
        obj.main()
        logger.info(f">>>>> Stage {STAGE_NAME} Finished")

    except Exception as e:
        logger.exception(e)
        raise e

from Classification.config.configuration import ConfigurationManager
from Classification.components.evaluation import Evaluation
from Classification import logger


STAGE_NAME = "Evaluation Model Stage"


class EvaluationModelStagePipeline:
    def __init__(self):
        pass


    def main(self):
        config= ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationModelStagePipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=========x")
    except Exception as e:
        logger.exception(e)
        raise 
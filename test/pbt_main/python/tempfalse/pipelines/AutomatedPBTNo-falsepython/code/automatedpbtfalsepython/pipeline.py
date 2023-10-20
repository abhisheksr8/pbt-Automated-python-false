from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from automatedpbtfalsepython.config.ConfigStore import *
from automatedpbtfalsepython.udfs.UDFs import *
from prophecy.utils import *
from automatedpbtfalsepython.graph import *

def pipeline(spark: SparkSession) -> None:
    df_s3_source_dataset = s3_source_dataset(spark)
    Lookup_1(spark, df_s3_source_dataset)
    df_Reformat_1 = Reformat_1(spark, df_s3_source_dataset)
    df_Script_1 = Script_1(spark, df_Reformat_1)
    df_SQLStatement_1 = SQLStatement_1(spark, df_s3_source_dataset)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/AutomatedPBTNo-falsepython")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/AutomatedPBTNo-falsepython", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/AutomatedPBTNo-falsepython")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()

from dagster import Definitions
from dagster_orchestration.assets.dbt_assets import dbt_project_assets
from dagster_dbt import DbtCliResource
from dagster_airbyte import AirbyteResource
from dagster_orchestration.assets.airbyte_assets import airbyte_assets_list
import os

DBT_PROJECT_DIR = "/Users/rahulmatade/end-to-end-data-engineering-project-4413618/dbt_transformation"
DBT_PROFILES_DIR = "/Users/rahulmatade/.dbt"

defs = Definitions(
    assets=[dbt_project_assets, airbyte_assets_list], 
    resources={
        "dbt": DbtCliResource(
            project_dir=DBT_PROJECT_DIR,
            profiles_dir=DBT_PROFILES_DIR,
        )
    }
)
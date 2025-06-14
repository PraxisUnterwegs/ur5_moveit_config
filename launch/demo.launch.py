from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_demo_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("ur5_robot", package_name="ur5_moveit_config").to_moveit_configs()

    # moveit_config = (MoveItConfigsBuilder("ur5_robot", package_name="ur5_moveit_config").planning_pipelines(["ompl", "lerp", "chomp", "pilz_industrial_motion_planner", "dmp"]).to_moveit_configs())

    # moveit_config = (
    #     MoveItConfigsBuilder("ur5_robot", package_name="ur5_moveit_config")
    #     .planning_pipelines(
    #         pipelines=["ompl", "lerp", "chomp", "pilz_industrial_motion_planner", "dmp"],
    #         default_planning_pipeline="ompl"  # Here should be a string, specifying the default planner
    #     )
    #     .to_moveit_configs()
    # )

    return generate_demo_launch(moveit_config)

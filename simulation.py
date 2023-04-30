import sys
from simso.configuration import Configuration
from simso.generator.task_generator import TaskGenerator
from simso.core import Model


def create_model(core_count: int, cluster_size: int):

    if cluster_size % core_count != 0:
        raise ValueError("Cluster size must be a multiple of core count")
    
    cluster_count = core_count // core_count

    configuration = Configuration()

    configuration.duration = 400 * configuration.cycles_per_ms

    for core_id in range(core_count):

        configuration.add_processor(name=f"core {core_id}", identifier=core_id)
    
    configuration.add_task(name="task 1", identifier=1, period=10)

    configuration.scheduler_info.clas = 'simso.schedulers.EDF'

    configuration.check_all()

    return Model(configuration)


if __name__ == '__main__':

    model = create_model(core_count=4, cluster_size=4)
    model.run_model()
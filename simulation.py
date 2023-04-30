import sys
from simso.configuration import Configuration
from collections import defaultdict
from simso.core import Model


def create_model(core_count: int, cluster_size: int):

    if core_count % cluster_size != 0:
        raise ValueError("Cluster size must be a multiple of core count")
    
    configuration = Configuration()

    configuration.duration = 400 * configuration.cycles_per_ms

    cluster_count = core_count // cluster_size
    cluster_cores = defaultdict(list)

    for core_id in range(core_count):

        configuration.add_processor(name=f"core {core_id}", identifier=core_id)
        cluster_cores[core_id % cluster_count].append(core_id)
    
    configuration.add_task(name="task 1", identifier=1, period=10)

    configuration.scheduler_info.clas = 'simso.schedulers.EDF'

    configuration.check_all()

    return Model(configuration)


if __name__ == '__main__':

    model = create_model(core_count=4, cluster_size=2)
    model.run_model()
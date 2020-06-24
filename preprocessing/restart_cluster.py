from dask.distributed import Client

client = Client(n_workers=100, threads_per_worker=55, processes=False, memory_limit='50GB')

client.restart()
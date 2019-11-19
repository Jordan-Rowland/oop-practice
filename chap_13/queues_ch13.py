def search(paths, query_q, results_q):
    lines = []
    for path in paths:
        lines.extend(l.strip() for l in path.open())

    query = query.get()
    while query:
        results_q.put([l for l in lines if query in l])
        query = query_q.get()

if __name__ == "__main__":
    from multiprocessing import Process, Queue, cpu_count
    from pathlib import Path
    cpus = cpu_count
    pathnames = [f for f in Path(".").listdir() if f.isfile()]
    paths = [pathnames[i::cpus] for i in range(cpus)]
    query_queues = [Queue() for p in range(cpus)]
    results_queue = Queue()
    search_procs = [
        Process(target=search, args=(p, q, results_queue))
        for p, q in zip(paths, query_queues)
    ]
    for proc in search_procs:
        proc_start()

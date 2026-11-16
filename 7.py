def allocate(blocks, processes, strategy):
    remaining = blocks[:]
    print("\n" + strategy)
    print("Process Size | Allocated Block")
    for process in processes:
        candidates = [i for i, size in enumerate(remaining)
                      if size >= process]
        if not candidates:
            print(f"{process:12} | Not Allocated")
            continue
        if strategy == "First Fit":
            index = candidates[0]
        elif strategy == "Best Fit":
            index = min(candidates, key=lambda i: remaining[i])
        else:
            index = max(candidates, key=lambda i: remaining[i])
        remaining[index] -= process
        print(f"{process:12} | Block {index + 1}")
    print("Remaining block sizes:", remaining)


if __name__ == "__main__":
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]
    print("Memory Blocks:", blocks)
    print("Processes:", processes)
    allocate(blocks, processes, "First Fit")
    allocate(blocks, processes, "Best Fit")
    allocate(blocks, processes, "Worst Fit")
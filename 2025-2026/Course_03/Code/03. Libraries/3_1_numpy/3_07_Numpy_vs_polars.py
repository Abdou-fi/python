# Numpy vs polars
import numpy as np
import polars as pl

# Numpy
np_array = np.array([1, 2, 3, 4, 5])
print(np_array)

# Polars
polars_df = pl.DataFrame({"a": [1, 2, 3, 4, 5]})
print(polars_df)

# Numpy operations
np_sum = np.sum(np_array)
print(f"Numpy Sum: {np_sum}")

# Polars operations
pl_sum = polars_df.select(pl.col("a").sum())
print(f"Polars Sum: {pl_sum}")

# compare numpy and polars execution speed for large data
import timeit
large_np_array = np.random.rand(1_000_000)
large_polars_df = pl.DataFrame({"a": large_np_array.tolist()})  
np_time = timeit.timeit(lambda: np.sum(large_np_array), number=100)
pl_time = timeit.timeit(lambda: large_polars_df.select(pl.col("a").sum()), number=100)
print(f"Numpy execution time: {np_time}")
print(f"Polars execution time: {pl_time}")
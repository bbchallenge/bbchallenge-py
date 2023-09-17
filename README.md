# bbchallenge-py

Python tooling to manipulate and visualise the Turing Machines of the bbchallenge project.

## Downloading the database

You can download the database of all 5-state undecided Turing machines here:

- [`https://dna.hamilton.ie/tsterin/all_5_states_undecided_machines_with_global_header.zip`](https://dna.hamilton.ie/tsterin/all_5_states_undecided_machines_with_global_header.zip)
- [`ipfs://QmcgucgLRjAQAjU41w6HR7GJbcte3F14gv9oXcf8uZ8aFM`](ipfs://QmcgucgLRjAQAjU41w6HR7GJbcte3F14gv9oXcf8uZ8aFM)
- [`https://ipfs.prgm.dev/ipfs/QmcgucgLRjAQAjU41w6HR7GJbcte3F14gv9oXcf8uZ8aFM`](https://ipfs.prgm.dev/ipfs/QmcgucgLRjAQAjU41w6HR7GJbcte3F14gv9oXcf8uZ8aFM)

The format of the database is described here: [https://github.com/bbchallenge/bbchallenge-seed](https://github.com/bbchallenge/bbchallenge-seed).

Database shasum: 
  1. `all_5_states_undecided_machines_with_global_header.zip`: `2576b647185063db2aa3dc2f5622908e99f3cd40`
  2. `all_5_states_undecided_machines_with_global_header`: `e57063afefd900fa629cfefb40731fd083d90b5e`
  
## Downloading the index of currently undecided machines

See https://github.com/bbchallenge/bbchallenge-undecided-index/

## Getting started

The notebook `BB5.ipynb` is currently self-contained.

You can install all the dependencies (including jupyter lab) by running the following:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## License

This work is dual-licensed under Apache 2.0 and MIT.
You can choose between one of them if you use this work.

`SPDX-License-Identifier: Apache-2.0 OR MIT`

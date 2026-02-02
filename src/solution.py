## Student Name:
## Student ID: 

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union
import math

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.

    """
    # TODO: Implement this function
    if not isinstance(resources, dict):
        raise ValueError("resources must be a dict")
    if not isinstance(requests, list):
        raise ValueError("requests must be a list of dicts")

    # Validate capacities + prepare totals
    totals: Dict[str, float] = {}
    for name, cap in resources.items():
        if not isinstance(name, str):
            raise ValueError("resource names must be strings")
        if not isinstance(cap, (int, float)) or isinstance(cap, bool):
            raise ValueError("resource capacities must be numeric")
        cap_f = float(cap)
        if math.isnan(cap_f) or cap_f < 0:
            raise ValueError("resource capacities must be non-negative and not NaN")
        totals[name] = 0.0

    # Accumulate demands
    for req in requests:
        if not isinstance(req, dict):
            raise ValueError("each request must be a dict")

        for rname, amt in req.items():
            # Unknown resource => infeasible
            if rname not in resources:
                return False

            if not isinstance(amt, (int, float)) or isinstance(amt, bool):
                raise ValueError("requested amounts must be numeric")
            amt_f = float(amt)
            if math.isnan(amt_f) or amt_f < 0:
                raise ValueError("requested amounts must be non-negative and not NaN")

            totals[rname] += amt_f

    # Check feasibility
    for rname, total in totals.items():
        if total > float(resources[rname]):
            return False

    return True

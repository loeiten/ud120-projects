#!/usr/bin/python

import numpy as np

def clean(elements, remove_indices):
    """
    Removes elments not in list

    Parameters
    ----------
    elements : iterable
        Elements to be cleaned
    remove_indices : iterable
        Indices to remove

    Returns
    -------
    cleaned_elements : list
        A list of the cleaned elements
    """

    cleaned_elements = [el for ind, el in enumerate(elements)\
                        if ind not in remove_indices]

    return cleaned_elements

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = np.abs((predictions - net_worths)/net_worths)
    # Get index numbers
    indices = list(range(len(errors)))
    # Sort in descending order
    errors_sorted, indices_sorted =\
        (list(x) for x in zip(*sorted(zip(errors, indices), reverse=True)))

    # Clean away the 10% of points that have the largest residual errors
    number_of_points_to_remove = int(round(0.1*len(predictions)))
    remove_indices = indices_sorted[:number_of_points_to_remove]

    cleaned_ages        = clean(ages       , remove_indices)
    cleaned_net_worths  = clean(net_worths , remove_indices)
    cleaned_errors      = clean(errors     , remove_indices)

    cleaned_data = list(zip(cleaned_ages, cleaned_net_worths, cleaned_errors))

    return cleaned_data

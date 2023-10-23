def BWT(n):
    # Add the magic end-of-string character
    n = n + "$"

    # Function to compute cyclic permutation
    def cyclic_permutation(n, i):
        return n[i:] + n[:i]
    
    # Build up the BWM from the cyclic permutations
    rows = [cyclic_permutation(n, i) for i in range(len(n))]

    # Use the builtin sort command to sort the cyclic permutations
    rows.sort()

    # Extract the last column
    bwt = "".join(row[-1] for row in rows)
    return bwt

# String to encode
n = "I_am_fully_convinced_that_species_are_not_immutable;_but_that_those_belonging_to_what_are_called_the_same_genera_are_lineal_descendants_of_some_other_and_generally_extinct_species,_in_the_same_manner_as_the_acknowledged_varieties_of_any_one_species_are_the_descendants_of_that_species._Furthermore,_I_am_convinced_that_natural_selection_has_been_the_most_important,_but_not_the_exclusive,_means_of_modification."

# Compute BWT
encoded_string = BWT(n)
print("Encoded string is:", encoded_string)


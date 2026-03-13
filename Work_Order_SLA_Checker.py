def get_sla_hours(priority):

    # Define the SLA mapping using a simple dictionary
    sla_mapping = {
        1: 4,
        2: 8,
        3: 24,
        4: 72
    }

    # Return the corresponding SLA hours, or -1 if priority is invalid
    return sla_mapping.get(priority, -1)


# Example usage
print(get_sla_hours(1))  # Output: 4
print(get_sla_hours(3))  # Output: 24
print(get_sla_hours(99)) # Output: -1
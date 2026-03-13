get_sla_hours() – Summary

The get_sla_hours(priority) function returns the SLA (Service Level Agreement) target hours based on a given priority value in IBM Maximo.
How It Works

A simple dictionary (sla_mapping) stores the SLA hours for each priority:

1 → 4 hours
2 → 8 hours
3 → 24 hours
4 → 72 hours

The function looks up the priority in the dictionary and returns the matching SLA hours.
If an invalid or unknown priority is passed (e.g., 99), the function safely returns -1.



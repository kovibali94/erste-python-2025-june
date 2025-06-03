yearly_salaries = [1000, 2000, 3000, 4000, 5000]

# A
stat = {
    "count": len(yearly_salaries),
    "sum": sum(yearly_salaries),
    "avg": sum(yearly_salaries) / len(yearly_salaries),
}

# B
salaries_len = len(yearly_salaries)
salaries_sum = sum(yearly_salaries)
stat = {
    "count": salaries_len,
    "sum": salaries_sum,
    "avg": salaries_sum / salaries_len,
}

# C
stat = {
    "count": (salaries_len := len(yearly_salaries)),
    "sum": (salaries_sum := sum(yearly_salaries)),
    "avg": salaries_sum / salaries_len,
}

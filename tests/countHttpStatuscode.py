from collections import Counter

def count_http_error_code(logs):
    status_counts = Counter()

    for log in logs:
        words = log.split()            # The status code is the word right after the word "status"
        code = words[words.index("status") + 1]
        status_counts[code] += 1

    for code, count in sorted(status_counts.items()):
        result = print(f"{code} : {count}")
    return result

logs = [
    "2026:16:15:00 time request GET status 200 ok",
    "2026:15:14:00 time response status 403 unauthorized",
    "2026:09:02:11 time request POST status 201 created",
    "2026:09:05:47 time request GET status 404 not found",
    "2026:10:30:15 time response status 500 internal server error",
    "2026:11:12:33 time request PUT status 204 no content",
    "2026:11:45:09 time request DELETE status 200 ok",
]

count_http_error_code(logs)

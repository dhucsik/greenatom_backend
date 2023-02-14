
def compare_versions(version1, version2):
    version1_split = [int(x) for x in version1.split(".")]
    version2_split = [int(x) for x in version2.split(".")]
    length = max(len(version1_split), len(version2_split))
    for i in range(length):
        if i >= len(version1_split):
            return -1
        if i >= len(version2_split):
            return 1
        if version1_split[i] > version2_split[i]:
            return 1
        if version1_split[i] < version2_split[i]:
            return -1
    return 0


print(compare_versions("1.0.0", "1.0.1"))
print(compare_versions("1.1.0", "1.0.1"))
print(compare_versions("1.0.1", "1.0.1"))
print(compare_versions("1.10.0", "1.1.0"))

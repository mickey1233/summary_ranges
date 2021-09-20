def summaryranges(nums):

    if not nums:
        print([])
    if len(nums) == 1:
        print([str(nums[0])])

    d, start, i = {}, nums[0], 1
    d[nums[0]] = nums[0]

    while i < len(nums):
        if nums[i] - nums[i - 1] == 1:
            d[start] = nums[i]
            i += 1
        else:
            start = nums[i]
            d[start] = start
            i += 1

    nums = sorted(d.items(), key=lambda x: x[0])
    d = []
    for i in nums:
        if i[0] == i[1]:
            d.append(str(i[0]))
        else:
            d.append(str(i[0]) + "->" + str(i[1]))
    print(d)


def main():
    summaryranges([0, 2, 3, 4, 6, 8, 9])
    summaryranges([])
    summaryranges([-1])
    summaryranges([0])
    summaryranges([0, 1, 2, 4, 5, 7])


if __name__ == "__main__":
    main()

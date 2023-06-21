class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(value, timestamp)]
        else:
            lst = self.map.get(key)
            lst.append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map.get(key)
        if not lst:
            return ""
        lo, hi = 0, len(lst) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            curr = lst[mid][1]
            if timestamp > curr:
                lo = mid + 1
            elif timestamp < curr:
                hi = mid - 1
            else:
                return lst[mid][0]
        return "" if hi < 0 else lst[hi][0]


if __name__ == '__main__':
    t = TimeMap()
    t.set("love","high",10)
    t.set("love","low",20)
    print(t.get("love", 5))  # expect ""
    print(t.get("love", 10))  # expect "high"
    print(t.get("love", 15))  # expect "high"
    print(t.get("love", 20))  # expect "low"
    print(t.get("love", 25))  # expect "low"
    # # store the key "foo" and value "bar" along with timestamp = 1.
    # t.set("foo", "bar", 1)
    # # return "bar"
    # print(t.get("foo", 1))
    # # return "bar", b/c no value corresponding to foo at timestamp 3 and timestamp 2, the only value is at timestamp 1 is "bar".
    # print(t.get("foo", 3))
    # # store the key "foo" and value "bar2" along with timestamp = 4.
    # t.set("foo", "bar2", 4)
    # print(t.get("foo", 4))         # return "bar2"
    # print(t.get("foo", 5))         # return "bar2"
    # store the key "foo" and value "bar" along with timestamp = 1.

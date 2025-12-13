# https://leetcode.com/problems/coupon-code-validator/?envType=daily-question&envId=2025-12-13
# Coupon Code Validator

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        valid_categories = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        pattern = re.compile(r'^[A-Za-z0-9_]+$')
        valid = []

        for c, b, active in zip(code, businessLine, isActive):
            if (
                active and
                c and
                pattern.match(c) and
                b in valid_categories
            ):
                valid.append((valid_categories[b], c))

        valid.sort(key=lambda x: (x[0], x[1]))

        return [c for _, c in valid]
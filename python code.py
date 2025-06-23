class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
      
        def calculate_gcd(a, b):
            """
            Helper function to calculate the Greatest Common Divisor (GCD) using recursion.
          
            :param a: First number
            :param b: Second number
            :return: GCD of a and b
            """
            return a if b == 0 else calculate_gcd(b, a % b)
      
        num_points = len(points)
        max_points_on_line = 1  # A single point is always on a line.
      
        for i in range(num_points):
            x1, y1 = points[i]
            slopes = Counter()  # Counter to track the number of points for each slope
            for j in range(i + 1, num_points):
                x2, y2 = points[j]
                delta_x = x2 - x1
                delta_y = y2 - y1
                gcd_value = calculate_gcd(delta_x, delta_y)
              
                # Reduce the slope to its simplest form to count all equivalent slopes together.
                slope = (delta_x // gcd_value, delta_y // gcd_value)
              
                # Increment the count for this slope and update the maximum if needed.
                slopes[slope] += 1
                max_points_on_line = max(max_points_on_line, slopes[slope] + 1)
              
        return max_points_on_line

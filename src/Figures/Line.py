import numpy as np
from src.Enums.LineEnum import LineEnum
class Line:
    def is_line(self, coordinate_point: list) -> LineEnum:
        """
        Determines the type of line based on the given coordinate points.

        Args:
            coordinate_point (list): A list of coordinate points that represent a line.

        Returns:
            LineEnum: The type of line represented by the LineEnum value.

        """
        if self._is_closed_line(coordinate_point):
            return LineEnum.CLOSED_LINE
        elif self._is_not_closed_line(coordinate_point):
            return LineEnum.NOT_CLOSED_LINE
        elif self._is_straight_line(coordinate_point):
            return LineEnum.STRAIGHT
        elif self._is_broken_line(coordinate_point):
            return LineEnum.BROKE_LINE
        elif self._is_curve_line(coordinate_point):
            return LineEnum.CURVE_LINE
        elif self._is_ray_line(coordinate_point):
            return LineEnum.RAY
        elif self._is_segment_line(coordinate_point):
            return LineEnum.SEGMENT
        else:
            return LineEnum.UNDEFINED

    def _is_closed_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points form a closed line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points form a closed line, False otherwise.
        """

        if len(coordinate_point) < 2:
            return False

        first_point = coordinate_point[0]
        last_point = coordinate_point[-1]

        return first_point[0] == last_point[0] and first_point[1] == last_point[1]

    def _is_not_closed_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points do not form a closed line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points do not form a closed line, False otherwise.
         """

        return not self._is_closed_line(coordinate_point)
    def _is_straight_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points form a straight line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points form a straight line, False otherwise.
        """
        if len(coordinate_point) < 2:
            return False
        
        # Check if all points lie on a straight line
        x0, y0 = coordinate_point[0]
        x1, y1 = coordinate_point[1]
        for i in range(2, len(coordinate_point)):
            x, y = coordinate_point[i]
            if (x - x0) * (y1 - y0) != (x1 - x0) * (y - y0):
                return False
        return True
    
    def _is_broken_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points form a broken line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points form a broken line, False otherwise.
        """

        if len(coordinate_point) < 2:
            return False

        for i in range(len(coordinate_point) - 2):
            x1, y1 = coordinate_point[i]
            x2, y2 = coordinate_point[i+1]
            x3, y3 = coordinate_point[i+2]

            if (x2 - x1) * (y3 - y2) != (x3 - x2) * (y2 - y1):
                return False

        return True

    def _is_curve_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points form a curve line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points form a curve line, False otherwise.
        """
         # Check if the line is not straight and not a closed line
        return not self._is_straight_line(coordinate_point) and not self._is_closed_line(coordinate_point)
    
    def _is_ray_line(self, coordinate_point: list) -> bool:
        """
        Checks if the given coordinate points form a ray line.

        Args:
            coordinate_point: A list of coordinate points.

        Returns:
            True if the given coordinate points form a ray line, False otherwise.
        """
        # Check if the line starts at a point and extends infinitely in one direction
        return not self._is_closed_line(coordinate_point) and len(coordinate_point) == 2
    
    def _is_segment_line(self, coordinate_point: list) -> bool:
        """
        Check if the given coordinate points form a finite segment between two points.

        Args:
            coordinate_point (list): A list of coordinate points.

        Returns:
            bool: True if the coordinate points form a finite segment between two points, False otherwise.
        """
        # Check if the line is a finite segment between two points
        return not self._is_closed_line(coordinate_point) and len(coordinate_point) == 2
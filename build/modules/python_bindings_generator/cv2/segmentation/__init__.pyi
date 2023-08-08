__all__: list[str] = []

import cv2
import cv2.typing
import typing


# Classes
class IntelligentScissorsMB:
    # Functions
    def __init__(self) -> None: ...

    def setWeights(self, weight_non_edge: float, weight_gradient_direction: float, weight_gradient_magnitude: float) -> IntelligentScissorsMB: ...

    def setGradientMagnitudeMaxLimit(self, gradient_magnitude_threshold_max: float = ...) -> IntelligentScissorsMB: ...

    def setEdgeFeatureZeroCrossingParameters(self, gradient_magnitude_min_value: float = ...) -> IntelligentScissorsMB: ...

    def setEdgeFeatureCannyParameters(self, threshold1: float, threshold2: float, apertureSize: int = ..., L2gradient: bool = ...) -> IntelligentScissorsMB: ...

    @typing.overload
    def applyImage(self, image: cv2.typing.MatLike) -> IntelligentScissorsMB: ...
    @typing.overload
    def applyImage(self, image: cv2.UMat) -> IntelligentScissorsMB: ...

    @typing.overload
    def applyImageFeatures(self, non_edge: cv2.typing.MatLike, gradient_direction: cv2.typing.MatLike, gradient_magnitude: cv2.typing.MatLike, image: cv2.typing.MatLike | None = ...) -> IntelligentScissorsMB: ...
    @typing.overload
    def applyImageFeatures(self, non_edge: cv2.UMat, gradient_direction: cv2.UMat, gradient_magnitude: cv2.UMat, image: cv2.UMat | None = ...) -> IntelligentScissorsMB: ...

    def buildMap(self, sourcePt: cv2.typing.Point) -> None: ...

    @typing.overload
    def getContour(self, targetPt: cv2.typing.Point, contour: cv2.typing.MatLike | None = ..., backward: bool = ...) -> cv2.typing.MatLike: ...
    @typing.overload
    def getContour(self, targetPt: cv2.typing.Point, contour: cv2.UMat | None = ..., backward: bool = ...) -> cv2.UMat: ...




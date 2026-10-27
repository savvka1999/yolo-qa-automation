def calculate_iou(boxA, boxB):
    """
    Считает IoU для двух рамок.
    Формат рамки: [x1, y1, x2, y2]
    """
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

def test_perfect_match():
    box_gt = [100, 100, 200, 200]
    box_pred = [100, 100, 200, 200]
    iou = calculate_iou(box_gt, box_pred)
    assert iou == 1.0

def test_no_match():
    box_gt = [100, 100, 200, 200]
    box_pred = [300, 300, 400, 400]
    iou = calculate_iou(box_gt, box_pred)
    assert iou == 0.0
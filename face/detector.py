from deepface import DeepFace


def detect_emotion(image_path):
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=["emotion"],
            enforce_detection=False
        )

        if isinstance(result, list):
            result = result[0]

        emotion = result["dominant_emotion"]

        confidence = round(
            result["emotion"][emotion],
            2
        )

        return {
            "emotion": emotion.capitalize(),
            "confidence": confidence
        }

    except Exception as e:
        return {
            "emotion": "Unknown",
            "confidence": 0,
            "error": str(e)
        }
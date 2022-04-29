import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5m, yolov5l, yolov5x, custom

# Images
# img = 'https://www.pinkvilla.com/files/styles/amp_metadata_content_image/public/gal_gadot_refused_a_sexualised_wonder_woman_scene_in_justice_league_but_joss_whedon_did_it_with_a_body_double.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img = "imgs\man1.png"
# Inference
results = model(img)
# labels, cord_thres = results.xyxyn[0][:, -1].numpy(), results.xyxyn[0][:, :-1].numpy()
# category = "2 : Person"
# class_name = category.split(':')[1].strip().lower()
print(results.pandas().xyxy[0])
# class_pred = results.pandas().xyxy[0].name
# percentage_pred = results.pandas().xyxy[0].confidence
# is_same = 0
# max_percentage = 0
# for i in range(len(class_pred)):
#     print()
#     if class_pred[i].lower() == class_name:
#         if percentage_pred[i] >= 0.60:
#             is_same = 1
#         elif percentage_pred[i] >= 0.30:
#             max_percentage = max(max_percentage,percentage_pred[i])
# print(is_same)
# print(max_percentage)


# for each in results.pandas().xyxy:
#     print(1)
#     print(each)
# print(labels)
# Results
results.show()

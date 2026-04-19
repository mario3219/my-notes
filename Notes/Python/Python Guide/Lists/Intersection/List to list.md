```
cta_train = set(cta_train_ids)
cta_test  = set(cta_test_ids)
wta_train = set(wta_train_ids)
wta_test  = set(wta_test_ids)

print(">>> Patients in CTA train and WTA train")
print(len(cta_train & wta_train))

print(">>> Patients in CTA train and WTA test")
print(len(cta_train & wta_test))

print(">>> Patients in WTA train and CTA test")
print(len(wta_train & cta_test))

print(">>> Patients in WTA train and WTA train")
print(len(wta_train))  # or len(wta_train & wta_train)
```

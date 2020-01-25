from distutils.dir_util import copy_tree

x = [('27043206-b89c-4f6d-8000-5302df3ee8b4'), ('ed4509f6-7187-4038-843a-1e458fa73b47'),
 ('a342b670-ac6d-4cbd-8c14-974342d1bb5b'), ('698cf633-0eaa-4d79-8065-babda50868d8'),
 ('d64d5e4b-183d-4e08-a418-0aec8e34a1b8'), ('04ded73b-eaad-430d-8a1a-ad1156a446ba'),
 ('d9cd950a-5622-4c88-a416-65335918e623'), ('f5d842bb-d9e2-4825-9286-f5ccf5edc277'),
 ('674b38c7-4b5e-4c44-a958-bcff82b81c1b'), ('df071ae7-0fb7-47d6-8804-deb1e8c7a1c8'),
 ('d18a92bf-ca79-4ddc-8b99-c645af7f0e12'), ('83d9d839-c5b4-459e-82ba-f697742a3c9d'),
 ('944000ed-7bb6-4b77-990b-79cc1b4a85af'), ('d91e640e-ce43-4173-9b91-eb1e8f38dca4'),
 ('4edec922-5e6b-4216-b87b-0fd3f7705073'), ('1573d2eb-cfc0-488a-9a52-7143ee174250'),
 ('203371a9-28ff-4154-b320-eff2ddb44192'), ('f54771d3-10a7-46d6-b890-833587f570a5'),
 ('5183a790-fc24-4f8e-a6ab-f761f9556294'), ('19171e02-4bf3-4026-b2b5-15d1d848d0d1'),
 ('489d8175-adc7-42f5-be7b-1fe6d46d3e03'), ('382e95ac-0632-41b8-aa43-d8a2ff03211f'),
 ('7f1b80b1-6e60-4a22-bd37-a300a6039cbe'), ('e63ca5db-0203-42f8-8bee-d4a0955bfabe'),
 ('d84d998f-5046-4d1b-a4b5-27fc0c458292'), ('6bb6193a-8b44-4cd3-83c9-310dc3e51318'),
 ('d025eae1-fc3a-4ee3-b280-cdcf3eea9d23'), ('722ab0d2-8ae5-4fde-b0ee-575502b3dfc3'),
 ('dca31841-60e0-4625-a9c2-472a91fbd1fe'), ('4b205541-2bc3-4d8a-a2db-43505264ddce'),
 ('6b13a8ba-8d3b-42f5-8629-b7f0283dca7f'), ('dc28b24c-b9f4-46a5-b14b-24d2ad110446'),
 ('b8b03931-d7e9-4e5a-aa03-55f1bf8004ee'), ('a5e63c76-f09f-4c93-9ea1-c050e66a6fb7'),
 ('d371aa19-86ae-4b8a-a9ef-ab08efffad99'), ('c2376fd4-7425-4c1f-ab5b-6354104897bd'),
 ('6c0f4d85-40d0-46f3-ae23-0cfe48c903f1'), ('002e45cc-282d-4af2-a5e4-9998719cb82c'),
 ('6527a6a9-f1de-4602-9353-b29ca84498d9'), ('2a45690a-2271-4369-98c0-ae52cc00f987'),
 ('cc881670-373a-4f2c-b0b2-fecb516982bd'), ('0f8f52d8-b78f-4904-b5e1-3e65136209b0'),
 ('6c46e75b-5906-40c2-be9b-bbfdf717660a'), ('4450c4be-605e-469e-b839-a0a73843bed7'),
 ('9f77c854-bbc0-461e-99d7-b69704c969a9'), ('301ab9e4-947f-49f1-a7f1-adb8303be0c8'),
 ('6bb3744d-6add-42d0-82f8-9d263c39bc63'), ('3ff5d8b9-d972-4a3c-8a78-af1ccd390d1c'),
 ('a4219c8f-305d-472e-bb01-6a0b8cbb81eb'), ('55f5306e-cf08-4e11-bc22-95347d553677')]

y = [elem for elem in x]

source_dir = '/home/sidravic/downloaded_images/v1'
destination_dir = '/home/sidravic/downloaded_images/internal'


for dirname in y:
    source_dir_full_path = f'{source_dir}/{dirname}'
    destination_dir_full_path = f'{destination_dir}/{dirname}'
    print(f'src: {source_dir_full_path}  dest: {destination_dir_full_path}')
    copy_tree(source_dir_full_path, destination_dir_full_path)
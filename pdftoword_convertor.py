# Import module
import groupdocs_conversion_cloud
# Get your app_sid and app_key at https://dashboard.groupdocs.cloud (free registration is required).
app_sid = “xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx”
app_key = “xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx”
# Create instance of the API
convert_api = groupdocs_conversion_cloud.ConvertApi.from_keys(app_sid, app_key)
file_api = groupdocs_conversion_cloud.FileApi.from_keys(app_sid, app_key)
try:
#upload soruce file to storage
 filename = ‘Sample.pdf’
 remote_name = ‘Sample.pdf’
 output_name= ‘sample.docx’
 strformat=’docx’
request_upload = groupdocs_conversion_cloud.UploadFileRequest(remote_name,filename)
 response_upload = file_api.upload_file(request_upload)
 #Convert PDF to Word document
 settings = groupdocs_conversion_cloud.ConvertSettings()
 settings.file_path =remote_name
 settings.format = strformat
 settings.output_path = output_name
 
 loadOptions = groupdocs_conversion_cloud.PdfLoadOptions()
 loadOptions.hide_pdf_annotations = True
 loadOptions.remove_embedded_files = False
 loadOptions.flatten_all_fields = True
settings.load_options = loadOptions
convertOptions = groupdocs_conversion_cloud.DocxConvertOptions()
convertOptions.from_page = 1
convertOptions.pages_count = 1
 
settings.convert_options = convertOptions
 
request = groupdocs_conversion_cloud.ConvertDocumentRequest(settings)
response = convert_api.convert_document(request)
print(“Document converted successfully: “ + str(response))
except groupdocs_conversion_cloud.ApiException as e:
 print(“Exception when calling get_supported_conversion_types: {0}”.format(e.message))

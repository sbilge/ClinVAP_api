
[![Docker: Available](https://img.shields.io/badge/hosted-docker--hub-blue.svg)](https://cloud.docker.com/u/personalizedoncology/repository/list)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

## ClinVAP REST API

1. Clone the repository  
`git clone --single-branch --branch clinvap-api-dev https://github.com/sbilge/ClinVAP_api.git`

2. Change directory into ClinVAP_api  
`cd ClinVAP_api`

3. Start application via  
`docker-compose up`

4. Connect to localhost

	4.1. Upload VCF file  
`localhost/upload-input`

	4.2. Download output  
`localhost/<filename>`

	`<filename>` extention should either be *.JSON* to download JSON file or *.DOCX*  to download Word file.

	E.g if the uploaded file name was *text.vcf*, use ***test.json*** or ***test.docx*** as `<filename>`.

	4.3. Get list of driver genes  
	`localhost/<filename>/tables/driver-genes`
	
	E.g if the uploaded file name was *text.vcf*, use ***test.json*** as `<filename>`.

	For detailed API documentation, see [API Documentation](#API Documentation)

5. Terminate the application via `CTRL+C`

6. To remove containers after terminating the application:  
`docker-compose down`

### API Documentation <a name="API Documentation"></a>
<https://app.swaggerhub.com/apis/sbilge/ClinVAP/1.0.0>


### Citation

If you use ClinVAP in your work, please cite the following article

* Sürün, B., Schärfe, C.P., Divine, M.R., Heinrich, J., Toussaint, N.C., Zimmermann, L., Beha, J. and Kohlbacher, O., 2020. ClinVAP: a reporting strategy from variants to therapeutic options. Bioinformatics, 36(7), pp.2316-2317.




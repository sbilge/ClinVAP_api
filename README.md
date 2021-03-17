
[![Docker: Available](https://img.shields.io/badge/hosted-docker--hub-blue.svg)](https://cloud.docker.com/u/personalizedoncology/repository/list)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

## ClinVAP REST API

1. Clone the repository  
`git clone --single-branch --branch master https://github.com/sbilge/ClinVAP_api.git`

2. Change directory into ClinVAP_api  
`cd ClinVAP_api`

3. Copy Ensembl VEP files to volume via

    * If you need human genome assembly GRCh37, use: `docker run -v clinvap_downloads:/mnt bilges/clinvap_file_deploy:vP_GRCh37`
    * If you need human genome assembly GRCh38, use: `docker run -v clinvap_downloads:/mnt bilges/clinvap_file_deploy:vP_GRCh38`

4. Start application via  
`docker-compose up`

5. Connect to localhost

	5.1. Upload input(s): VCF file, list of copy number variants (optional), genome assembly version (default is GRCh37), diagnosis (optional), filtering option based on diagnosis (optional) 
    `localhost/upload-input`   

    5.2. Check the status
    `localhost/results/<filename>/status`

        E.g if the uploaded file name was *test.vcf*, use ***test.vcf*** as `<filename>`.

	5.3. Download SNV output
    `localhost/results/<filename>`

	    `<filename>` extention should be *.JSON* to download JSON file.

	    E.g if the uploaded file name was *text.vcf*, use ***test.json***.

    5.4. Download CNV output (output is generated if CNV list is provided as input)
    `localhost/results/<filename>`

	    `<filename>` extention should be *cnv.JSON* to download JSON file.

	    E.g if the uploaded file name was *text.vcf*, use ***test.cnv.json***.

	5.5. Get list of driver genes   
    `localhost/results/<filename>/tables/driver-genes`
	
	    E.g if the uploaded file name was *test.vcf*, use ***test.json*** as `<filename>`.

	    For detailed API documentation, see [API Documentation](#API Documentation)

6. Terminate the application via `CTRL+C`

7. To remove containers after terminating the application:  
`docker-compose down`

### API Documentation <a name="API Documentation"></a>
<https://app.swaggerhub.com/apis/sbilge/ClinVAP/1.0.0>


### Citation

If you use ClinVAP in your work, please cite the following article

* Sürün, B., Schärfe, C.P., Divine, M.R., Heinrich, J., Toussaint, N.C., Zimmermann, L., Beha, J. and Kohlbacher, O., 2020. ClinVAP: a reporting strategy from variants to therapeutic options. Bioinformatics, 36(7), pp.2316-2317.




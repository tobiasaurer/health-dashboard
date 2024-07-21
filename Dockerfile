#Using python
FROM tobes95/python_dash_base:latest
# Using Layered approach for the installation of requirements
COPY environment/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
#Copy files to your container
COPY . ./
#Running your APP and doing some PORT Forwarding
CMD gunicorn -b 0.0.0.0:80 main:main
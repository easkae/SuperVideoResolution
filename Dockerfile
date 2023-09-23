FROM python:3.11.4
LABEL authors="zabar"
WORKDIR /app

COPY . .
RUN pip install -r req.txt
RUN python main_test_swinir.py --task real_sr --scale 4 --model_path model_zoo/swinir/003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN.pth --folder_lq testsets/myset/lr
RUN python ./vidsave.py

CMD /bin/bash -c "while true;do echo 'alive...';sleep 30s;done"

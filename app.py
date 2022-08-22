
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

from FFT.fft import FFT
from RandomTS.randomTs import RandomTS

app = Flask(__name__)
app.debug = True
CORS(app)
api = Api(app)

class Welcome(Resource):
    def get(self):    
        return "Welcome to Airborne FFT"

class FFTDecompose(Resource):
    def get(self):
        #Generate a time series
        randomTsWithPeriodicity = RandomTS().tsValues
        
        #Instantiate the FFT class perform first the Fourier Transform and then 2) the inverse FFT
        fftInst = FFT()
        fftInst.fft(randomTsWithPeriodicity) 

        #The fftInst will exposure exported data members as properties to protect the source
        return jsonify({
            "original": list(randomTsWithPeriodicity),
            "periodicity": list(fftInst.periodicity),
            "noise": list(fftInst.noise),
            "psd": list(fftInst.psd) 
        }) 

api.add_resource(FFTDecompose, "/fftdecompose")
api.add_resource(Welcome, "/welcome")



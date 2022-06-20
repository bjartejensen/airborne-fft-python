
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

from FFT.fft import FFT
from RandomTS.randomTs import RandomTS

app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self) ->str:
        return "Hello world!"

class FFTDecompose(Resource):
    def get(self):
        print("HEJS")
        #Generate a time series
        randomTsWithPeriodicity = RandomTS().generateTS()
        
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
api.add_resource(HelloWorld, "/helloworld")



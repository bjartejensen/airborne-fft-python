

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from numpy import ndarray
from Brunton.brunton import Brunton
from FFT.fft import FFTLocal


app = Flask(__name__)
CORS(app)
api = Api(app)

class FFTDecompose(Resource):
    def get(self):
        
        bruntonInst = Brunton()
        originalTs= bruntonInst.generateRandomnessTS()
        
        fftInst = FFTLocal()
        fftInst.fft(originalTs) #Note: return power spectrum density as is.
        
        return jsonify({
            "original": list(originalTs),
            "periodicity": list(fftInst.periodicity),
            "trend": list(fftInst.periodicity),
            "noise": list(fftInst.noise),
            "psd": list(fftInst.psd.real)
        }) 




api.add_resource(FFTDecompose, "/fftdecompose")



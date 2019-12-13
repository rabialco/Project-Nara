from django.db import models

class mark(models.Model):
	nilai_choice = [
		(4.0, ('A')),
		(3.7, ('A-')),
		(3.3, ('B+')),
		(3.0, ('B')),
		(2.7, ('B-')),
		(2.3, ('C+')),
		(2.0, ('C')),
		(1.0, ('D')),
		(0.0, ('E')),
	]
	mata_kuliah = models.CharField(blank=False, max_length=30)
	sks = models.IntegerField(blank=False, max_length=None, default=0)
	nilai = models.FloatField(blank=False, choices=nilai_choice)
	semester = models.IntegerField(blank=False, max_length=None, default=0)

	def getData(self):
		return{
			'mata_kuliah' : self.mata_kuliah,
			'sks' : self.sks,
			'nilai' : self.nilai,
			'semester' : self.semester,
		}
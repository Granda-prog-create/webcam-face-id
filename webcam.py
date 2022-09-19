import cv2
import mediapipe as mp 

#Inicializar opencv e mediapipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils 

#Ler a imagem da webcam
while webcam.isOpened():
    validacao, frame = webcam.read() 
    if not validacao:
        break
    imagem = frame
    lista_rostos = reconhecedor_rosto.process(imagem) # usa o reconhecedor para criar uma lista com os rostos reconhecidos
    
    if lista_rostos.detections: # caso algum rosto tenha sido reconhecido
        for rosto in lista_rostos.detections: # para cada rosto que foi reconhecido
            desenho.draw_detection(imagem, rosto) # desenha o rosto na imagem
    
    cv2.imshow("Webcam com Python", imagem) # mostra a imagem da webcam para a gente
    if cv2.waitKey(5) == 27: # ESC # garante que o código vai ser pausado ao apertar ESC (código 27) e que o código vai esperar 5 milisegundos a cada leitura da webcam
        break
webcam.release() # encerra a conexão com a webcam
cv2.destroyAllWindows() # fecha a janela que mostra o que a webcam está vendo


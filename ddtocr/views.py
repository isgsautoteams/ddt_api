from django.http import JsonResponse

def extract_text_and_tables(request):
    if request.method == 'POST':
        # Assuming the image file is passed as 'image' in the request
        image = request.FILES['image']

        # Process the image using your deepdoctection script
        # Replace this with your actual processing logic
        extraction_result = process_image(image)

        # Return the extraction result as JSON
        return JsonResponse({'result': extraction_result})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

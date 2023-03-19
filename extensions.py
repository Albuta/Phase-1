extension = input("Please enter your file extension \n")

match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
      print("image/png")
    case "pdf":
       print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("Please choose an extension from this list: gif, jpg, jpeg, png, pdf, txt, zip")

<?php
session_start();

$ALLOWED = ['png', 'jpeg', 'gif', 'pdf', 'zip'];

function is_valid_extension($filename) {
    global $ALLOWED;
    $ext = explode('.', $filename)[1];
    foreach ($ALLOWED as $allowed_ext) {
        if (stripos($ext, $allowed_ext) !== false) {
            return true;
        }
    }
    return false;
}

$message = '';
$message_type = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['password']) && $_POST['password'] === "supersecret1234564_niceeeee132213") {
        $_SESSION['auth'] = true;
        $message = "Login successful!";
        $message_type = "success";
    }

    if (isset($_FILES['file']) && $_SESSION['auth'] === true) {
        $file = $_FILES['file'];
        $filename = $file['name'];
        $tmpname = $file['tmp_name'];
        $mime = mime_content_type($tmpname);

        $allowed_mimes = [
            'image/png',
            'image/jpeg',
            'image/gif',
            'application/zip',
            'application/pdf'
        ];

        if (!in_array($mime, $allowed_mimes)) {
            $message = "Invalid MIME type!";
            $message_type = "error";
        } elseif (!is_valid_extension($filename)) {
            $message = "Invalid file extension!";
            $message_type = "error";
        } else {
            $ext = pathinfo($filename, PATHINFO_EXTENSION);
            $newname = bin2hex(random_bytes(8)) . '.' . $ext;
            move_uploaded_file($tmpname, "uploads/" . $newname);
            $message = "File uploaded successfully: /uploads/$newname";
            $message_type = "success";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anonymous File Upload</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1rem;
        }

        .form-group {
            margin-bottom: 25px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            text-align: left;
        }

        .form-control {
            width: 100%;
            padding: 15px;
            border: 2px solid #e1e5e9;
            border-radius: 10px;
            font-size: 16px;
            transition: all 0.3s ease;
            background: white;
        }

        .form-control:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }

        .file-input-wrapper {
            position: relative;
            display: inline-block;
            width: 100%;
        }

        .file-input {
            position: absolute;
            left: -9999px;
        }

        .file-input-label {
            display: block;
            padding: 15px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .file-input-label:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .btn {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
            margin-top: 10px;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .btn:active {
            transform: translateY(0);
        }

        .message {
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            font-weight: 600;
        }

        .message.success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .message.error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        .allowed-files {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
            text-align: left;
        }

        .allowed-files h4 {
            color: #333;
            margin-bottom: 10px;
        }

        .file-types {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .file-type {
            background: #667eea;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        .upload-area {
            border: 2px dashed #667eea;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }

        .upload-area:hover {
            border-color: #764ba2;
            background: rgba(102, 126, 234, 0.05);
        }

        .upload-icon {
            font-size: 3rem;
            color: #667eea;
            margin-bottom: 15px;
        }

        @media (max-width: 480px) {
            .container {
                padding: 20px;
            }
            
            .logo {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo">📁 Anonymous Upload</div>
        <div class="subtitle">Secure file sharing made simple</div>

        <?php if ($message): ?>
            <div class="message <?php echo $message_type; ?>">
                <?php echo htmlspecialchars($message); ?>
            </div>
        <?php endif; ?>

        <?php if (!isset($_SESSION['auth']) || $_SESSION['auth'] !== true): ?>
            <form method="POST">
                <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" id="password" name="password" class="form-control" placeholder="Enter password" required>
                </div>
                <button type="submit" class="btn">🔐 Login</button>
            </form>
        <?php else: ?>
            <form method="POST" enctype="multipart/form-data">
                <div class="upload-area">
                    <div class="upload-icon">📤</div>
                    <div class="file-input-wrapper">
                        <input type="file" name="file" id="file" class="file-input" required>
                        <label for="file" class="file-input-label">Choose File or Drag & Drop</label>
                    </div>
                </div>
                <button type="submit" class="btn">🚀 Upload File</button>
            </form>

            <div class="allowed-files">
                <h4>📋 Allowed File Types:</h4>
                <div class="file-types">
                    <span class="file-type">PNG</span>
                    <span class="file-type">JPEG</span>
                    <span class="file-type">GIF</span>
                    <span class="file-type">PDF</span>
                    <span class="file-type">ZIP</span>
                </div>
            </div>
        <?php endif; ?>
    </div>

    <script>
        const fileInput = document.getElementById('file');
        const fileLabel = document.querySelector('.file-input-label');
        
        if (fileInput && fileLabel) {
            fileInput.addEventListener('change', function() {
                if (this.files.length > 0) {
                    fileLabel.textContent = `Selected: ${this.files[0].name}`;
                } else {
                    fileLabel.textContent = 'Choose File or Drag & Drop';
                }
            });

            const uploadArea = document.querySelector('.upload-area');
            
            uploadArea.addEventListener('dragover', function(e) {
                e.preventDefault();
                this.style.borderColor = '#764ba2';
                this.style.background = 'rgba(102, 126, 234, 0.1)';
            });

            uploadArea.addEventListener('dragleave', function(e) {
                e.preventDefault();
                this.style.borderColor = '#667eea';
                this.style.background = 'transparent';
            });

            uploadArea.addEventListener('drop', function(e) {
                e.preventDefault();
                this.style.borderColor = '#667eea';
                this.style.background = 'transparent';
                
                const files = e.dataTransfer.files;
                if (files.length > 0) {
                    fileInput.files = files;
                    fileLabel.textContent = `Selected: ${files[0].name}`;
                }
            });
        }
    </script>
</body>
</html>
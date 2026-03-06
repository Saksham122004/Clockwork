import cv2
import os
import argparse


def banner():
    print(r"""
████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗██╗ ██████╗ █████╗ ██╗     
╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██║██╔════╝██╔══██╗██║     
   ██║   █████╗  ██║     ███████║██╔██╗ ██║██║██║     ███████║██║     
   ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║██║     ██╔══██║██║       
   ██║   ███████╗╚██████╗██║  ██║██║ ╚████║██║╚██████╗██║  ██║███████╗
   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

                    
                    ███████╗ █████╗ ███╗   ███╗
                    ██╔════╝██╔══██╗████╗ ████║
                    ███████╗███████║██╔████╔██║
                    ╚════██║██╔══██║██║╚██╔╝██║
                    ███████║██║  ██║██║ ╚═╝ ██║
                    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                    
          
                        TECHNICAL SAM
                Video Micro Frame Extractor
""")


def extract_micro_frames(video_path, interval, output_dir):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print(f"\nVideo FPS: {fps}")
    print(f"Total Frames: {total_frames}")

    frame_interval = int(fps * interval)

    if frame_interval <= 0:
        frame_interval = 1

    os.makedirs(output_dir, exist_ok=True)

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count % frame_interval == 0:
            timestamp = frame_count / fps

            filename = os.path.join(
                output_dir,
                f"frame_{saved_count:06d}_{timestamp:.6f}s.jpg"
            )

            cv2.imwrite(filename, frame)
            print(f"[+] Saved {filename}")

            saved_count += 1

        frame_count += 1

    cap.release()

    print("\nExtraction Complete")
    print(f"Frames saved: {saved_count}")
    print(f"Output folder: {output_dir}")


def main():
    banner()

    parser = argparse.ArgumentParser(
        description="Micro Frame Video Forensic Extractor"
    )

    parser.add_argument(
        "video",
        help="Path to video file"
    )

    parser.add_argument(
        "-i", "--interval",
        type=float,
        default=0.01,
        help="Frame interval in seconds (default: 0.01)"
    )

    parser.add_argument(
        "-o", "--output",
        default="frames_output",
        help="Output folder"
    )

    args = parser.parse_args()

    extract_micro_frames(args.video, args.interval, args.output)


if __name__ == "__main__":
    main()
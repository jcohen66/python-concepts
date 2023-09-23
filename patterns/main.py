class ExporterFactory(ABC):
    """
    factory that represents a combination of video and auto codecs.

    Args:
        ABC (_type_): _description_
    """
    
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        pass
    
    def get_audio_exporter(self) -> AudioExporter:
        pass
    
class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
    
class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slow speed, high quality export."""
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
    
class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export."""
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()
    
def read_exporter() -> ExporterFactory:
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    # read the desired export quality
    while True:
        export_quality = input("Enter desired quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")
    
    
def main():
    """Main function"""
    pass

if __name__ == "__main__":
    main()
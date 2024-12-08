import { useGet } from '@/core/react-query';
import { useEffect } from 'react';

type UseDownloadProps = {
  folderName: string;
  source: string;
  downloadFileName: string;
};

const useDownload = ({
  folderName,
  source,
  downloadFileName,
}: UseDownloadProps) => {
  const { mutateAsync, isSuccess, data, isPending } = useGet<string, undefined>(
    `/download-folder${folderName}/${source}`,
    'download',
    undefined,
    { responseType: 'blob' },
  );

  useEffect(() => {
    if (isSuccess) {
      const blob = new Blob([data.data], {
        type: data.headers['content-type'],
      });
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = `${downloadFileName}.zip`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(link.href);
    }
  }, [isSuccess, data]);

  const download = async () => {
    return await mutateAsync(undefined);
  };

  return { download, isSuccess, isPending };
};

export default useDownload;

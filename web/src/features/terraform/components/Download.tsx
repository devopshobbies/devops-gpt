import useDownload from '../../../hooks/useDownload';
import { DownloadFolders } from '../../constants';
import { useEffect } from 'react';
import useGptStore from '../../../utils/store';

const Download = () => {
  const setGeneratorQuery = useGptStore((s) => s.setGeneratorQuery);

  const { downloadFile, isSuccess, endpoint, downloadRef } = useDownload(
    DownloadFolders.MY_TERRAFORM,
  );

  useEffect(() => {
    if (isSuccess) {
      downloadFile();
      setGeneratorQuery(false, '');
    }
  }, [isSuccess, endpoint, downloadFile, setGeneratorQuery]);

  return <a ref={downloadRef} style={{ display: 'none' }} />;
};

export default Download;

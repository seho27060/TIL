package com.ssafy.specificPJ.Domain.DTO;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.List;

@Getter
@Builder
public class PageCDTO {
    List<ChallengeResponseDTO> challengeResponseDTOList;
    boolean hasNext;
    int totalPages;
    int currentPage;
    int size;
}
